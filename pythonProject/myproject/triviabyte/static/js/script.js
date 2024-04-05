/*methods: {
    getQuestions() {
        var _this = this
        fetch(`/api/get-quiz/?gfg=${this.gfg}`)
        .then(response => response.json())
        .then(result => {
            console.log("Received questions data:", result.data)
            _this.questions = result.data
        })
    },
    checkAnswer(event, uid) {
        console.log("Selected answer:", event.target.value, "Question UID:", uid)

        this.questions.forEach(question => {
            question.answer.forEach(answer => {
                if (answer.answer === event.target.value) {
                    if (answer.is_correct) {
                        console.log('Your answer is correct!')
                        alert("Hurray your answer is correct!")
                    } else {
                        console.log('Your answer is wrong!')
                        alert("Better luck next time!")
                    }
                }
            })
        })
    },
    nextQuestion() {
        this.currentQuestionIndex++
        console.log("Moving to question:", this.currentQuestionIndex)
    },
    restartQuiz() {
        this.currentQuestionIndex = 0
        console.log("Restarting quiz...")
    }
},