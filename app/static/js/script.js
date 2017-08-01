var jogador = 'x';
var jogada = 0;
function checando(id) {
  var src = chequesrc(id);
  var cpu = document.getElementById('cpu').checked;
  if (src == "branco.png") {
    document.getElementById(id).src = "../static/img/" + jogador + ".png";
    jogada++;
    if (chequeVitoria()) {
      alert ("parece que você é bom nisso, vitória pro " + jogador);
      location.reload();
    }
      if(jogada >= 9){
        alert('JOGO EMPATADO!');
        location.reload();
    }
    if (jogador == 'x') {
      jogador = 'o';
    }
    else {
      jogador = 'x';
    }
  }
  if (cpu && jogador == 'o') {
    checando(jogadaDoComputador());
  }
}
function jogadaDoComputador(){
  if (chequesrc('n5') == 'branco.png') {
    return 'n5'
  }
  if (chequesrc('n3') == 'branco.png') {
    return 'n3'
  }
  if (chequesrc('n9') == 'branco.png') {
    return 'n9'
  }
  if (chequesrc('n1') == 'branco.png') {
    return 'n1'
  }
  if (chequesrc('n7') == 'branco.png') {
    return 'n7'
  }
  if (chequesrc('n8') == 'branco.png') {
    return 'n8'
  }
  return 'n' + Math.floor((Math.random() * 9) + 1);
}

function chequesrc(id) {
  var src = document.getElementById(id).src;
  return src.substring(src.length -10, src.length);

}
function chequeVitoria() {
  if ((chequesrc('n1') == chequesrc('n2')) && (chequesrc('n1') == chequesrc('n3')) && chequesrc('n1') != 'branco.png'){
    return true;
  }
  if ((chequesrc('n4') == chequesrc('n5')) && (chequesrc('n4') == chequesrc('n6')) && chequesrc('n4') != 'branco.png'){
    return true;
  }
  if ((chequesrc('n7') == chequesrc('n8')) && (chequesrc('n7') == chequesrc('n9')) && chequesrc('n7') != 'branco.png'){
    return true;
  }
  if ((chequesrc('n7') == chequesrc('n5')) && (chequesrc('n7') == chequesrc('n3')) && chequesrc('n7') != 'branco.png'){
    return true;
  }
  if ((chequesrc('n1') == chequesrc('n5')) && (chequesrc('n1') == chequesrc('n9')) && chequesrc('n1') != 'branco.png'){
    return true;
  }
  if ((chequesrc('n1') == chequesrc('n4')) && (chequesrc('n1') == chequesrc('n7')) && chequesrc('n1') != 'branco.png'){
    return true;
  }
  if ((chequesrc('n2') == chequesrc('n5')) && (chequesrc('n2') == chequesrc('n8')) && chequesrc('n2') != 'branco.png'){
    return true;
  }
  if ((chequesrc('n3') == chequesrc('n6')) && (chequesrc('n3') == chequesrc('n9')) && chequesrc('n3') != 'branco.png'){
    return true;
  }
  return false;

}
