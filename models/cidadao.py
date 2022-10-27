from sql_alchemy import banco

class ModelProprietario(banco.Model):
    __tablename__ =   'proprietario'
    
    id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    moldelo = banco.Column(banco.String(80))
    cor = banco.Column(banco.String(80))
    
    def get(self, id, nome, modelo, cor):
        self.id = id
        self.nome = nome
        self.modelo = modelo
        self.cor = cor
    
    def json(self):
        return {
            'id': self.id,
            'Nome': self.nome,
            'Modelo': self.modelo,
            'Cor': self.cor
        }
    
    @classmethod
    def find_modelo(cls, modelo):
        modelo = cls.qyery.filter_by(modelo=modelo).count()
        if modelo:
            return modelo
        return None

    @classmethod
    def find_id(cls, id):
        dono = cls.query.filter_by(id=id)
        if id:
            return id
        return None

    def save_cadastro(self):
        banco.session.add(self)
        banco.session.commit()
        
    def update_car(self, nome, modelo, cor):
        self.nome = nome
        self.modelo = modelo
        self.cor = cor
        
    def delete_dados(self):
        banco.session.delete(self)
        banco.session.commit()