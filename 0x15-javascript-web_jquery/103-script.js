$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/?lang=' + languageCode;
    $.getJSON(url, function (data) {
      $('#hello').text(data.hello);
    });
  });

  $('#language_code').on('keydown', function (e) {
    if (e.keyCode === 13) {
      $('#btn_translate').click();
    }
  });
});