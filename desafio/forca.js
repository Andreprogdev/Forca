class Forca {
  palavra
  letrasChutadas
  vidas
  palavras
  constructor(palavra) {
    this.palavra = palavra
    this.letrasChutadas = []
    this.vidas = 6
    this.palavras = []
    for(let c = 0; c < this.palavra.length; c++){
    this.palavras.push("-")
    }
  }


  chutar(chute) {
    if(chute.length == 1 && isNaN(+chute) && !this.letrasChutadas.includes(chute)){
      this.letrasChutadas.push(chute);
      if(this.palavra.includes(chute)) {
        this.verificar(chute)
      }else{
        this.vidas--;
      }
    }else{
      console.log('Por favor, só coloque uma letra');    
    }
    }
   

  buscarEstado() {
    if (this.vidas == 0) {
      return "perdeu"
    } else if (this.palavra == this.palavras.join("")) {
      return "ganhou"
    } 
    return "aguardando chute";
  }

  buscarDadosDoJogo() {
    return {
      letrasChutadas: this.letrasChutadas,
      vidas: this.vidas,
      palavras: this.palavras.join("")
    }
  }

  verificar(chute){  
    for(let c = 0; c < this.palavra.length; c++){
        if(this.palavra[c] == chute){
          this.palavras[c] = chute
        }
      }
  }a

}

module.exports = Forca;
