var jogador = 'x';
var jogada = 0;
function checando(id) {
  var src = chequesrc(id);
  if (src == "branco.png") {
    document.getElementById(id).src = "/home/luana/projeto/app/static/img"+ jogador + ".png";
    jogada++;
    if (chequeVitoria()) {
      alert ("Parece que você é bom nisso " + jogador);
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
