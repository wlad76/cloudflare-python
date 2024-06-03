# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.magic_transit import (
    AppListResponse,
    AppCreateResponse,
    AppDeleteResponse,
    AppUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        app = client.magic_transit.apps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.magic_transit.apps.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.magic_transit.apps.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.apps.with_raw_response.create(
                account_id="",
                body={},
            )

    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        app = client.magic_transit.apps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.magic_transit.apps.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.magic_transit.apps.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.apps.with_raw_response.create(
                account_id="",
                body={},
            )

    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        app = client.magic_transit.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.magic_transit.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.magic_transit.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_app_id` but received ''"):
            client.magic_transit.apps.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        app = client.magic_transit.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.magic_transit.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.magic_transit.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_app_id` but received ''"):
            client.magic_transit.apps.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    def test_method_update_overload_3(self, client: Cloudflare) -> None:
        app = client.magic_transit.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    def test_raw_response_update_overload_3(self, client: Cloudflare) -> None:
        response = client.magic_transit.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_3(self, client: Cloudflare) -> None:
        with client.magic_transit.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_app_id` but received ''"):
            client.magic_transit.apps.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    def test_method_update_overload_4(self, client: Cloudflare) -> None:
        app = client.magic_transit.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    def test_raw_response_update_overload_4(self, client: Cloudflare) -> None:
        response = client.magic_transit.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_4(self, client: Cloudflare) -> None:
        with client.magic_transit.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_app_id` but received ''"):
            client.magic_transit.apps.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        app = client.magic_transit.apps.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[AppListResponse], app, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.apps.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(SyncSinglePage[AppListResponse], app, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.apps.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(SyncSinglePage[AppListResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.apps.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        app = client.magic_transit.apps.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_transit.apps.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_transit.apps.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.apps.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_app_id` but received ''"):
            client.magic_transit.apps.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncApps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.magic_transit.apps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.apps.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.apps.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.apps.with_raw_response.create(
                account_id="",
                body={},
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.magic_transit.apps.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.apps.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.apps.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.apps.with_raw_response.create(
                account_id="",
                body={},
            )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.magic_transit.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_app_id` but received ''"):
            await async_client.magic_transit.apps.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.magic_transit.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_app_id` but received ''"):
            await async_client.magic_transit.apps.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.magic_transit.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_app_id` but received ''"):
            await async_client.magic_transit.apps.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.magic_transit.apps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.apps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.apps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.apps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_app_id` but received ''"):
            await async_client.magic_transit.apps.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.magic_transit.apps.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[AppListResponse], app, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.apps.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AsyncSinglePage[AppListResponse], app, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.apps.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AsyncSinglePage[AppListResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.apps.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.magic_transit.apps.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.apps.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.apps.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.apps.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_app_id` but received ''"):
            await async_client.magic_transit.apps.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
