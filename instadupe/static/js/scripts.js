$(document).ready(function () {
  $('button[type="submit"]').click(function () {
    $('input[name="avatar"]').click();
  });
  $('input[name="avatar"]').change(function () {
    $("#change-avatar").submit();
  });
});
