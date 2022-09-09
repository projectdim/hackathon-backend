from fastapi import APIRouter

router = APIRouter(prefix="/markers")


@router.get()
def get_all_markers():
    return [
        {
            "longitude": 2000,
            "latitude": 3000
        }, {
            "longitude": 2500,
            "latitude": 3400
        },
    ]
