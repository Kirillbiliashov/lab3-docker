from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

from spaceship.config import Settings
from spaceship.routers import api, health

import numpy as np


def make_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        debug=settings.debug,
        title=settings.app_title,
        description=settings.app_description,
        version=settings.app_version,
    )
    app.state.settings = settings

    if settings.debug:
        app.mount('/static', StaticFiles(directory='build'), name='static')

    app.include_router(api.router, prefix='/api', tags=['api'])
    app.include_router(health.router, prefix='/health', tags=['health'])

    @app.get('/', include_in_schema=False, response_class=FileResponse)
    async def root() -> str:
        return 'build/index.html'

   @app.get('/matrix')
    def multiply_matrices():
    matrix1 = np.random.rand(10, 10)
    matrix2 = np.random.rand(10, 10)
    product = np.dot(matrix1, matrix2)
    result = {
         "matrix_a": matrix1.tolist(),
         "matrix_b": matrix2.tolist(),
         "product": product.tolist()
     }
    return result	

    return app
