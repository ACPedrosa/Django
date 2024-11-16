from .templates import (
    home_view,
    cadastro_view,
    sucess_view,
    participante_view,
    perfil_view
)

from .api import ParticipanteListView, ParticipanteDetailView

__all__ = [
    "home_view",
    "cadastro_view",
    "sucess_view",
    "participante_view",
    "perfil_view",
    "ParticipanteListView",
    "ParticipanteDetailView",
]
