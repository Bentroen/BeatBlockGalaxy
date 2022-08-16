from typing import Dict, List
from beet import Context, Model


def multipart_model(prefix: str, models: List[str]) -> Model:
    def multipart_base() -> Dict:
        return {"parent": f"{prefix}/base", "overrides": []}

    def multipart_predicate(cmd: int, model: str) -> Dict:
        return {"predicate": {"custom_model_data": cmd}, "model": model}

    multipart = multipart_base()
    for id, model in enumerate(models):
        predicate = multipart_predicate(id + 1, f"{prefix}/{model}")
        multipart["overrides"].append(predicate)

    return Model(multipart)


def base_model() -> Model:
    return Model(
        {
            "elements": [
                {
                    "from": [0, 0, 0],
                    "to": [16, 16, 16],
                    "faces": {
                        "up": {"uv": [0, 0, 16, 16], "texture": "#texture"},
                        "down": {"uv": [0, 0, 16, 16], "texture": "#texture"},
                        "north": {"uv": [0, 0, 16, 16], "texture": "#texture"},
                        "south": {"uv": [0, 0, 16, 16], "texture": "#texture"},
                        "east": {"uv": [0, 0, 16, 16], "texture": "#texture"},
                        "west": {"uv": [0, 0, 16, 16], "texture": "#texture"},
                    },
                }
            ],
            "display": {
                "thirdperson_righthand": {
                    "rotation": [0, 0, 0],
                    "translation": [-30, -26, -28],
                    "scale": [4, 4, 4],
                },
            },
        }
    )


def custom_model(texture: str) -> Model:
    return Model(
        {
            "parent": "beatblock:block/base",
            "textures": {"texture": f"beatblock:block/{texture}"},
        }
    )


def generate(ctx: Context) -> None:

    states = [
        "solid",
        "yellow_on",
        "yellow_off",
        "yellow_flashing",
        "green_on",
        "green_off",
        "green_flashing",
    ]

    for state in states:
        ctx.assets[f"beatblock:block/{state}"] = custom_model(texture=state)

    ctx.assets["beatblock:block/base"] = base_model()
    ctx.assets["minecraft:item/stone"] = multipart_model("beatblock:block", states)
