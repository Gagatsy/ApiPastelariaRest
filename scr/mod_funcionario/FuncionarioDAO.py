from fastapi import APIRouter, Depends, HTTPException
from mod_funcionario.Funcionario import Funcionario
import db
from mod_funcionario.FuncionarioModel import FuncionarioDB
import security

router = APIRouter(dependencies=[Depends(security.verify_token), Depends(security.verify_key)])

@router.get("/funcionario/", tags=["Funcionário"])
def get_funcionarios():
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).all()
        return dados
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()

@router.get("/funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).all()
        if not dados:
            raise HTTPException(status_code=404, detail="Funcionário não encontrado")
        return dados
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()

@router.post("/funcionario/", tags=["Funcionário"])
def create_funcionario(corpo: Funcionario):
    try:
        session = db.Session()
        dados = FuncionarioDB(None, corpo.nome, corpo.matricula, corpo.cpf, corpo.telefone, corpo.grupo, corpo.senha)
        session.add(dados)
        session.commit()
        return {"id": dados.id_funcionario}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()

@router.put("/funcionario/{id}", tags=["Funcionário"])
def update_funcionario(id: int, corpo: Funcionario):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one_or_none()
        if not dados:
            raise HTTPException(status_code=404, detail="Funcionário não encontrado")
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        dados.senha = corpo.senha
        dados.matricula = corpo.matricula
        dados.grupo = corpo.grupo
        session.commit()
        return {"id": dados.id_funcionario}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()

@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one_or_none()
        if not dados:
            raise HTTPException(status_code=404, detail="Funcionário não encontrado")
        session.delete(dados)
        session.commit()
        return {"id": dados.id_funcionario}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()
@router.put("/funcionario/{id}", tags=["Funcionário"])
def update_funcionario(id: int, corpo: Funcionario):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one_or_none()
        if not dados:
            raise HTTPException(status_code=404, detail="Funcionário não encontrado")
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        dados.senha = corpo.senha
        dados.matricula = corpo.matricula
        dados.grupo = corpo.grupo
        session.commit()
        return {"id": dados.id_funcionario}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()
