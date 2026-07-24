import httpx

from schemas.cocktail import CocktailRead


class CocktailApiClient:
    def __init__(
        self,
        base_url: str,
        timeout: float,
    ):
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=timeout,
        )

    async def get_cocktail_by_id(self, cocktail_id: int) -> CocktailRead | None:
        response = await self._client.get(f"/cocktails/{cocktail_id}")

        if response.status_code == 404:
            return None

        response.raise_for_status()

        cocktail_data = response.json()

        cocktail = CocktailRead(**cocktail_data)

        return cocktail

    async def close(self) -> None:
        await self._client.aclose()

