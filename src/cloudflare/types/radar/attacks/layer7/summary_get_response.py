# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from ....unnamed_schema_ref_b5f3bd1840490bc487ffef84567807b1 import UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1
from ....unnamed_schema_ref_baac9d7da12de53e99142f8ecd3982e5 import UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5

__all__ = ["SummaryGetResponse", "Meta", "MetaConfidenceInfo", "Summary0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRefB5f3bd1840490bc487ffef84567807b1]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[UnnamedSchemaRefBaac9d7da12de53e99142f8ecd3982e5] = FieldInfo(alias="dateRange")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Summary0(BaseModel):
    access_rules: str = FieldInfo(alias="ACCESS_RULES")

    api_shield: str = FieldInfo(alias="API_SHIELD")

    bot_management: str = FieldInfo(alias="BOT_MANAGEMENT")

    data_loss_prevention: str = FieldInfo(alias="DATA_LOSS_PREVENTION")

    ddos: str = FieldInfo(alias="DDOS")

    ip_reputation: str = FieldInfo(alias="IP_REPUTATION")

    waf: str = FieldInfo(alias="WAF")


class SummaryGetResponse(BaseModel):
    meta: Meta

    summary_0: Summary0
