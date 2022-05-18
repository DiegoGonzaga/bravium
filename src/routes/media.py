from fastapi import APIRouter, status, Response

router = APIRouter(prefix="/media")

media_examples = {"1": "Livro", "2": "Mangá", "3": "Filme"}


@router.get("/")
async def media():
    return {"message": "Media"}


@router.get("/{id}")
async def get_media(id, response: Response):
    print(id)
    if id not in media_examples.keys():
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Media not found."}
    return {"Media": media_examples[id]}
