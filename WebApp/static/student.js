// function to get the next question from the choices table of the database
function getQuestion() {
    $.ajax({
        url: '/get_question',
        type: 'GET',
        success: function(response) {
            $('#question').text(response.question);
            $('#choice1').text(response.choice1);
            $('#choice2').text(response.choice2);
            $('#choice3').text(response.choice3);
            $('#choice4').text(response.choice4);
        }
    });
}
    
