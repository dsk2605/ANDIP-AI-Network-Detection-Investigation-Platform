import time

from fastapi import Request

from app.core.logging import get_logger

logger = get_logger(__name__)


async def log_requests(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    duration = (time.perf_counter() - start_time) * 1000

    logger.info(
        "%s %s | Status=%d | %.2f ms",
        request.method,
        request.url.path,
        response.status_code,
        duration,
    )

    return response