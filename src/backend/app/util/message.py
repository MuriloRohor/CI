from fastapi import status
from fastapi.responses import RedirectResponse
from urllib.parse import quote

def adicionar_cookie_mensagem(response, mensagem):
    msg = quote(mensagem)
    response.set_cookie(
        key="mensagem",
        value=msg,
        max_age=20,
        samesite="Lax",
    )
    
def redirecionar_com_mensagem(url_destino: str, mensagem: str):
    response = RedirectResponse(
        url_destino,
        status_code=status.HTTP_303_SEE_OTHER,
    )
    adicionar_cookie_mensagem(response, mensagem)
    return response