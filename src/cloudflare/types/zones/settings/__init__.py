# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .nel_edit_params import NELEditParams as NELEditParams
from .ssl_edit_params import SSLEditParams as SSLEditParams
from .waf_edit_params import WAFEditParams as WAFEditParams
from .ipv6_edit_params import IPV6EditParams as IPV6EditParams
from .webp_edit_params import WebPEditParams as WebPEditParams
from .zone_setting_nel import ZoneSettingNEL as ZoneSettingNEL
from .zone_setting_ssl import ZoneSettingSSL as ZoneSettingSSL
from .zone_setting_waf import ZoneSettingWAF as ZoneSettingWAF
from .http2_edit_params import HTTP2EditParams as HTTP2EditParams
from .http3_edit_params import HTTP3EditParams as HTTP3EditParams
from .zone_setting_0rtt import ZoneSetting0rtt as ZoneSetting0rtt
from .zone_setting_ipv6 import ZoneSettingIPV6 as ZoneSettingIPV6
from .zone_setting_webp import ZoneSettingWebP as ZoneSettingWebP
from .brotli_edit_params import BrotliEditParams as BrotliEditParams
from .cipher_edit_params import CipherEditParams as CipherEditParams
from .minify_edit_params import MinifyEditParams as MinifyEditParams
from .mirage_edit_params import MirageEditParams as MirageEditParams
from .polish_edit_params import PolishEditParams as PolishEditParams
from .zone_setting_fonts import ZoneSettingFonts as ZoneSettingFonts
from .zone_setting_http2 import ZoneSettingHTTP2 as ZoneSettingHTTP2
from .zone_setting_http3 import ZoneSettingHTTP3 as ZoneSettingHTTP3
from .tls_1_3_edit_params import TLS1_3EditParams as TLS1_3EditParams
from .zone_setting_brotli import ZoneSettingBrotli as ZoneSettingBrotli
from .zone_setting_minify import ZoneSettingMinify as ZoneSettingMinify
from .zone_setting_mirage import ZoneSettingMirage as ZoneSettingMirage
from .zone_setting_polish import ZoneSettingPolish as ZoneSettingPolish
from .zero_rtt_edit_params import ZeroRTTEditParams as ZeroRTTEditParams
from .zone_setting_ciphers import ZoneSettingCiphers as ZoneSettingCiphers
from .zone_setting_tls_1_3 import ZoneSettingTLS1_3 as ZoneSettingTLS1_3
from .websocket_edit_params import WebsocketEditParams as WebsocketEditParams
from .early_hint_edit_params import EarlyHintEditParams as EarlyHintEditParams
from .zone_setting_buffering import ZoneSettingBuffering as ZoneSettingBuffering
from .zone_setting_nel_param import ZoneSettingNELParam as ZoneSettingNELParam
from .zone_setting_ssl_param import ZoneSettingSSLParam as ZoneSettingSSLParam
from .zone_setting_waf_param import ZoneSettingWAFParam as ZoneSettingWAFParam
from .cache_level_edit_params import CacheLevelEditParams as CacheLevelEditParams
from .pseudo_ipv4_edit_params import PseudoIPV4EditParams as PseudoIPV4EditParams
from .zone_setting_0rtt_param import ZoneSetting0rttParam as ZoneSetting0rttParam
from .zone_setting_ipv6_param import ZoneSettingIPV6Param as ZoneSettingIPV6Param
from .zone_setting_webp_param import ZoneSettingWebPParam as ZoneSettingWebPParam
from .zone_setting_websockets import ZoneSettingWebsockets as ZoneSettingWebsockets
from .font_setting_edit_params import FontSettingEditParams as FontSettingEditParams
from .zone_setting_cache_level import ZoneSettingCacheLevel as ZoneSettingCacheLevel
from .zone_setting_early_hints import ZoneSettingEarlyHints as ZoneSettingEarlyHints
from .zone_setting_http2_param import ZoneSettingHTTP2Param as ZoneSettingHTTP2Param
from .zone_setting_http3_param import ZoneSettingHTTP3Param as ZoneSettingHTTP3Param
from .zone_setting_pseudo_ipv4 import ZoneSettingPseudoIPV4 as ZoneSettingPseudoIPV4
from .always_online_edit_params import AlwaysOnlineEditParams as AlwaysOnlineEditParams
from .browser_check_edit_params import BrowserCheckEditParams as BrowserCheckEditParams
from .challenge_ttl_edit_params import ChallengeTTLEditParams as ChallengeTTLEditParams
from .rocket_loader_edit_params import RocketLoaderEditParams as RocketLoaderEditParams
from .zone_setting_brotli_param import ZoneSettingBrotliParam as ZoneSettingBrotliParam
from .zone_setting_minify_param import ZoneSettingMinifyParam as ZoneSettingMinifyParam
from .zone_setting_mirage_param import ZoneSettingMirageParam as ZoneSettingMirageParam
from .zone_setting_polish_param import ZoneSettingPolishParam as ZoneSettingPolishParam
from .image_resizing_edit_params import ImageResizingEditParams as ImageResizingEditParams
from .ip_geolocation_edit_params import IPGeolocationEditParams as IPGeolocationEditParams
from .security_level_edit_params import SecurityLevelEditParams as SecurityLevelEditParams
from .zone_setting_advanced_ddos import ZoneSettingAdvancedDDoS as ZoneSettingAdvancedDDoS
from .zone_setting_always_online import ZoneSettingAlwaysOnline as ZoneSettingAlwaysOnline
from .zone_setting_browser_check import ZoneSettingBrowserCheck as ZoneSettingBrowserCheck
from .zone_setting_challenge_ttl import ZoneSettingChallengeTTL as ZoneSettingChallengeTTL
from .zone_setting_ciphers_param import ZoneSettingCiphersParam as ZoneSettingCiphersParam
from .zone_setting_rocket_loader import ZoneSettingRocketLoader as ZoneSettingRocketLoader
from .zone_setting_tls_1_3_param import ZoneSettingTLS1_3Param as ZoneSettingTLS1_3Param
from .min_tls_version_edit_params import MinTLSVersionEditParams as MinTLSVersionEditParams
from .mobile_redirect_edit_params import MobileRedirectEditParams as MobileRedirectEditParams
from .security_header_edit_params import SecurityHeaderEditParams as SecurityHeaderEditParams
from .ssl_recommender_edit_params import SSLRecommenderEditParams as SSLRecommenderEditParams
from .tls_client_auth_edit_params import TLSClientAuthEditParams as TLSClientAuthEditParams
from .zone_setting_image_resizing import ZoneSettingImageResizing as ZoneSettingImageResizing
from .zone_setting_ip_geolocation import ZoneSettingIPGeolocation as ZoneSettingIPGeolocation
from .zone_setting_security_level import ZoneSettingSecurityLevel as ZoneSettingSecurityLevel
from .always_use_https_edit_params import AlwaysUseHTTPSEditParams as AlwaysUseHTTPSEditParams
from .development_mode_edit_params import DevelopmentModeEditParams as DevelopmentModeEditParams
from .orange_to_orange_edit_params import OrangeToOrangeEditParams as OrangeToOrangeEditParams
from .prefetch_preload_edit_params import PrefetchPreloadEditParams as PrefetchPreloadEditParams
from .zone_setting_buffering_param import ZoneSettingBufferingParam as ZoneSettingBufferingParam
from .zone_setting_min_tls_version import ZoneSettingMinTLSVersion as ZoneSettingMinTLSVersion
from .zone_setting_mobile_redirect import ZoneSettingMobileRedirect as ZoneSettingMobileRedirect
from .zone_setting_security_header import ZoneSettingSecurityHeader as ZoneSettingSecurityHeader
from .zone_setting_ssl_recommender import ZoneSettingSSLRecommender as ZoneSettingSSLRecommender
from .zone_setting_tls_client_auth import ZoneSettingTLSClientAuth as ZoneSettingTLSClientAuth
from .browser_cache_ttl_edit_params import BrowserCacheTTLEditParams as BrowserCacheTTLEditParams
from .email_obfuscation_edit_params import EmailObfuscationEditParams as EmailObfuscationEditParams
from .h2_prioritization_edit_params import H2PrioritizationEditParams as H2PrioritizationEditParams
from .zone_setting_always_use_https import ZoneSettingAlwaysUseHTTPS as ZoneSettingAlwaysUseHTTPS
from .zone_setting_development_mode import ZoneSettingDevelopmentMode as ZoneSettingDevelopmentMode
from .zone_setting_orange_to_orange import ZoneSettingOrangeToOrange as ZoneSettingOrangeToOrange
from .zone_setting_prefetch_preload import ZoneSettingPrefetchPreload as ZoneSettingPrefetchPreload
from .zone_setting_websockets_param import ZoneSettingWebsocketsParam as ZoneSettingWebsocketsParam
from .hotlink_protection_edit_params import HotlinkProtectionEditParams as HotlinkProtectionEditParams
from .proxy_read_timeout_edit_params import ProxyReadTimeoutEditParams as ProxyReadTimeoutEditParams
from .response_buffering_edit_params import ResponseBufferingEditParams as ResponseBufferingEditParams
from .zone_setting_browser_cache_ttl import ZoneSettingBrowserCacheTTL as ZoneSettingBrowserCacheTTL
from .zone_setting_cache_level_param import ZoneSettingCacheLevelParam as ZoneSettingCacheLevelParam
from .zone_setting_early_hints_param import ZoneSettingEarlyHintsParam as ZoneSettingEarlyHintsParam
from .zone_setting_email_obfuscation import ZoneSettingEmailObfuscation as ZoneSettingEmailObfuscation
from .zone_setting_h2_prioritization import ZoneSettingH2Prioritization as ZoneSettingH2Prioritization
from .zone_setting_pseudo_ipv4_param import ZoneSettingPseudoIPV4Param as ZoneSettingPseudoIPV4Param
from .opportunistic_onion_edit_params import OpportunisticOnionEditParams as OpportunisticOnionEditParams
from .server_side_exclude_edit_params import ServerSideExcludeEditParams as ServerSideExcludeEditParams
from .zone_setting_hotlink_protection import ZoneSettingHotlinkProtection as ZoneSettingHotlinkProtection
from .zone_setting_proxy_read_timeout import ZoneSettingProxyReadTimeout as ZoneSettingProxyReadTimeout
from .zone_setting_advanced_ddos_param import ZoneSettingAdvancedDDoSParam as ZoneSettingAdvancedDDoSParam
from .zone_setting_always_online_param import ZoneSettingAlwaysOnlineParam as ZoneSettingAlwaysOnlineParam
from .zone_setting_browser_check_param import ZoneSettingBrowserCheckParam as ZoneSettingBrowserCheckParam
from .zone_setting_challenge_ttl_param import ZoneSettingChallengeTTLParam as ZoneSettingChallengeTTLParam
from .zone_setting_opportunistic_onion import ZoneSettingOpportunisticOnion as ZoneSettingOpportunisticOnion
from .zone_setting_rocket_loader_param import ZoneSettingRocketLoaderParam as ZoneSettingRocketLoaderParam
from .zone_setting_server_side_exclude import ZoneSettingServerSideExclude as ZoneSettingServerSideExclude
from .true_client_ip_header_edit_params import TrueClientIPHeaderEditParams as TrueClientIPHeaderEditParams
from .zone_setting_image_resizing_param import ZoneSettingImageResizingParam as ZoneSettingImageResizingParam
from .zone_setting_ip_geolocation_param import ZoneSettingIPGeolocationParam as ZoneSettingIPGeolocationParam
from .zone_setting_security_level_param import ZoneSettingSecurityLevelParam as ZoneSettingSecurityLevelParam
from .zone_setting_min_tls_version_param import ZoneSettingMinTLSVersionParam as ZoneSettingMinTLSVersionParam
from .zone_setting_mobile_redirect_param import ZoneSettingMobileRedirectParam as ZoneSettingMobileRedirectParam
from .zone_setting_security_header_param import ZoneSettingSecurityHeaderParam as ZoneSettingSecurityHeaderParam
from .zone_setting_ssl_recommender_param import ZoneSettingSSLRecommenderParam as ZoneSettingSSLRecommenderParam
from .zone_setting_tls_client_auth_param import ZoneSettingTLSClientAuthParam as ZoneSettingTLSClientAuthParam
from .zone_setting_true_client_ip_header import ZoneSettingTrueClientIPHeader as ZoneSettingTrueClientIPHeader
from .automatic_https_rewrite_edit_params import AutomaticHTTPSRewriteEditParams as AutomaticHTTPSRewriteEditParams
from .origin_max_http_version_edit_params import OriginMaxHTTPVersionEditParams as OriginMaxHTTPVersionEditParams
from .zone_setting_always_use_https_param import ZoneSettingAlwaysUseHTTPSParam as ZoneSettingAlwaysUseHTTPSParam
from .zone_setting_development_mode_param import ZoneSettingDevelopmentModeParam as ZoneSettingDevelopmentModeParam
from .zone_setting_orange_to_orange_param import ZoneSettingOrangeToOrangeParam as ZoneSettingOrangeToOrangeParam
from .zone_setting_prefetch_preload_param import ZoneSettingPrefetchPreloadParam as ZoneSettingPrefetchPreloadParam
from .opportunistic_encryption_edit_params import OpportunisticEncryptionEditParams as OpportunisticEncryptionEditParams
from .origin_max_http_version_get_response import OriginMaxHTTPVersionGetResponse as OriginMaxHTTPVersionGetResponse
from .zone_setting_browser_cache_ttl_param import ZoneSettingBrowserCacheTTLParam as ZoneSettingBrowserCacheTTLParam
from .zone_setting_email_obfuscation_param import ZoneSettingEmailObfuscationParam as ZoneSettingEmailObfuscationParam
from .zone_setting_h2_prioritization_param import ZoneSettingH2PrioritizationParam as ZoneSettingH2PrioritizationParam
from .origin_max_http_version_edit_response import OriginMaxHTTPVersionEditResponse as OriginMaxHTTPVersionEditResponse
from .zone_setting_automatic_https_rewrites import (
    ZoneSettingAutomaticHTTPSRewrites as ZoneSettingAutomaticHTTPSRewrites,
)
from .zone_setting_hotlink_protection_param import (
    ZoneSettingHotlinkProtectionParam as ZoneSettingHotlinkProtectionParam,
)
from .zone_setting_opportunistic_encryption import (
    ZoneSettingOpportunisticEncryption as ZoneSettingOpportunisticEncryption,
)
from .zone_setting_proxy_read_timeout_param import ZoneSettingProxyReadTimeoutParam as ZoneSettingProxyReadTimeoutParam
from .zone_setting_opportunistic_onion_param import (
    ZoneSettingOpportunisticOnionParam as ZoneSettingOpportunisticOnionParam,
)
from .zone_setting_server_side_exclude_param import (
    ZoneSettingServerSideExcludeParam as ZoneSettingServerSideExcludeParam,
)
from .origin_error_page_pass_thru_edit_params import (
    OriginErrorPagePassThruEditParams as OriginErrorPagePassThruEditParams,
)
from .sort_query_string_for_cache_edit_params import (
    SortQueryStringForCacheEditParams as SortQueryStringForCacheEditParams,
)
from .zone_setting_origin_error_page_pass_thru import (
    ZoneSettingOriginErrorPagePassThru as ZoneSettingOriginErrorPagePassThru,
)
from .zone_setting_sort_query_string_for_cache import (
    ZoneSettingSortQueryStringForCache as ZoneSettingSortQueryStringForCache,
)
from .zone_setting_true_client_ip_header_param import (
    ZoneSettingTrueClientIPHeaderParam as ZoneSettingTrueClientIPHeaderParam,
)
from .automatic_platform_optimization_edit_params import (
    AutomaticPlatformOptimizationEditParams as AutomaticPlatformOptimizationEditParams,
)
from .zone_setting_automatic_https_rewrites_param import (
    ZoneSettingAutomaticHTTPSRewritesParam as ZoneSettingAutomaticHTTPSRewritesParam,
)
from .zone_setting_opportunistic_encryption_param import (
    ZoneSettingOpportunisticEncryptionParam as ZoneSettingOpportunisticEncryptionParam,
)
from .zone_setting_automatic_platform_optimization import (
    ZoneSettingAutomaticPlatformOptimization as ZoneSettingAutomaticPlatformOptimization,
)
from .zone_setting_origin_error_page_pass_thru_param import (
    ZoneSettingOriginErrorPagePassThruParam as ZoneSettingOriginErrorPagePassThruParam,
)
from .zone_setting_sort_query_string_for_cache_param import (
    ZoneSettingSortQueryStringForCacheParam as ZoneSettingSortQueryStringForCacheParam,
)
from .zone_setting_automatic_platform_optimization_param import (
    ZoneSettingAutomaticPlatformOptimizationParam as ZoneSettingAutomaticPlatformOptimizationParam,
)
from .unnamed_schema_ref_b234e6a28c1a1c7c29213787c0621eaa import (
    UnnamedSchemaRefB234e6a28c1a1c7c29213787c0621eaa as UnnamedSchemaRefB234e6a28c1a1c7c29213787c0621eaa,
)
