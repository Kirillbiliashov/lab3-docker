import numpy as np
from fastapi import APIRouter

router = APIRouter()

@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get('/matrix')
def multiply_matrices() -> dict:
    matrix1 = np.random.rand(10, 10)
    matrix2 = np.random.rand(10, 10)
    product = np.dot(matrix1, matrix2)
    return {
        "matrix_a": matrix1.tolist(),
        "matrix_b": matrix2.tolist(),
        "product": product.tolist()
    }
