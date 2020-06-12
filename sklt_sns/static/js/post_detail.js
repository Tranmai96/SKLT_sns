
$(document).ready(function () {
    function getCookie(name) {
    var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
  });
  //ここまでおまじないと思って記述
  //以下Ajax
  $("#Ine").click(function (event) {
    event.preventDefault();
    var ine = $(this);
    $.ajax({
        url: ine.attr('data-href'),
        method: 'POST',
        timeout: 10000,
        dataType: "json",
    })
    .done(function (data) {
        $('#ine').addClass('on')
        $('.ine-count').text('(' + data.count + ')' + ' ');
        $('.ine-msg').text(data.msg)
    })
    .fail(function (data) {
        alert("fail");
    })
  });
  