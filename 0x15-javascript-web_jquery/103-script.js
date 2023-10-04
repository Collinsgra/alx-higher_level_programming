const url = 'https://www.fourtonfish.com/hellosalut/hello/';

$(document).ready(function () {
  $('input#btn_translate').click(function () {
    $.get(url + $('input#language_code').val(), function (info) {
      $('div#hello').text(info.hello);
    });
  });

  $('#language_code').keydown(function (e) {
    if (e.keyCode === 13) {
      $.get(url + $('input#language_code').val(), function (info) {
        $('div#hello').text(info.hello);
      });
    }
