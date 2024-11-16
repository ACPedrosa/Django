from .templates import (
    home,
    cadastro_view,
    sucess_page,
    participante_page,
    perfil_view
)

from .api import ParticipanteListView, ParticipanteDetailView

__all__ = [
    "home",
    "cadastro_view",
    "sucess_page",
    "participante_page",
    "perfil_view",
    "ParticipanteListView",
    "ParticipanteDetailView",
]
