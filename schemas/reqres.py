from voluptuous import ALLOW_EXTRA
from voluptuous import Schema

login_unsuccessfull = Schema(
    {
        "error": "Missing password"
    },
    extra=ALLOW_EXTRA,
    required=True
)

create_user = Schema({
    "name": str,
    "job": str,
    "id": str,
    "createdAt": str
})
