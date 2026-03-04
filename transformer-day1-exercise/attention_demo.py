import numpy as np


def _softmax(logits: np.ndarray, axis: int = -1) -> np.ndarray:
    """
    Numerically stable softmax.
    """
    shifted = logits - np.max(logits, axis=axis, keepdims=True)
    exp_shifted = np.exp(shifted)
    return exp_shifted / np.sum(exp_shifted, axis=axis, keepdims=True)


def scaled_dot_product_attention(
    Q: np.ndarray,
    K: np.ndarray,
    V: np.ndarray,
) -> np.ndarray:
    """
    Compute scaled dot-product attention.

    Args:
        Q: Queries of shape (n_queries, d_k)
        K: Keys of shape (n_keys, d_k)
        V: Values of shape (n_keys, d_v)

    Returns:
        Attention output of shape (n_queries, d_v)
    """
    if Q.ndim != 2 or K.ndim != 2 or V.ndim != 2:
        raise ValueError("Q, K, and V must be 2D arrays.")

    n_queries, d_k_q = Q.shape
    n_keys, d_k_k = K.shape
    n_values, d_v = V.shape

    if d_k_q != d_k_k:
        raise ValueError(
            f"Q and K must have the same key dimension. Got {d_k_q} and {d_k_k}."
        )
    if n_keys != n_values:
        raise ValueError(
            f"K and V must have the same number of rows. Got {n_keys} and {n_values}."
        )

    scale = np.sqrt(d_k_q)
    similarity_scores = (Q @ K.T) / scale
    attention_weights = _softmax(similarity_scores, axis=-1)
    output = attention_weights @ V

    return output


if __name__ == "__main__":
    rng = np.random.default_rng(seed=42)

    n_queries = 3
    n_keys = 4
    d_k = 5
    d_v = 6

    Q = rng.normal(size=(n_queries, d_k))
    K = rng.normal(size=(n_keys, d_k))
    V = rng.normal(size=(n_keys, d_v))

    attention_out = scaled_dot_product_attention(Q=Q, K=K, V=V)

    print("Attention output:")
    print(attention_out)
    print("\nOutput shape:", attention_out.shape)
