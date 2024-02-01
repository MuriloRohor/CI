from sqlalchemy import select

from ci_app.database.models.FilialModel import Filial
from ci_app.database.models.StatusModel import Status
from ci_app.database.models.UserModel import User
from ci_app.database.models.CiModel import CorrespondenciaInterna

def test_create(session):
    new_filial = Filial(
        nome="Filial Iconha",
        cod_filial=1,
        cnpj=12345678912345,
        uf= "es",
        cep=2928000,
        rua="Rua de Tal",
        bairro="Centro",
        numero=209
    )
    session.add(new_filial)
    session.commit()
    filial = session.scalar(
        select(Filial).where(
            Filial.id == 1
        )
    )
    
    new_status = Status(
        cod_status=1,
        nome="Aguardando coleta"
    )
    session.add(new_status)
    session.commit()
    status = session.scalar(
        select(Status).where(
            Status.id == 1
        )
    )
    
    new_user = User(
        cod_matricula="0001",
        nome="João do Teste",
        email="joao@email.com",
        senha="password",
        token="abc-def-ghi",
        image_url="dir/image.png",
        filial_id = filial.id
    )
    new_user_2 = User(
        cod_matricula="0002",
        nome="Pedro do Teste",
        email="pedro@email.com",
        senha="password",
        token="abc-def-ghi",
        image_url="dir/image.png",
        filial_id = filial.id
    )
    session.add(new_user)
    session.add(new_user_2)
    session.commit()
    user_1 = session.scalar(
        select(User).where(
            User.id == 1
        )
    )
    user_2 = session.scalar(
        select(User).where(
            User.id == 2
        )
    )
    
    new_ci = CorrespondenciaInterna(
        cod_ci=1,
        user_id_remetente=user_1.id,
        user_id_destinatario=user_2.id,
        descricao="envelope cor marrom",
        status=1
    )
    session.add(new_ci)
    session.commit()
    corres = session.scalar(
        select(CorrespondenciaInterna)\
            .where(
            CorrespondenciaInterna.id == 1
            )
    )
    
    assert filial is not None
    assert status is not None
    assert user_1 is not None
    assert user_2 is not None
    assert filial is not None
    assert corres is not None
    
    
