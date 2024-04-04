const app = Vue.createApp({
    data() {
        return {
            currentQuestionIndex: 0,
            selectedOption: '',
            questions: [],
            showScore: false,
            score: 0
        };
    },
    methods: {
        fetchQuestions() {
            // Fetch questions from the server
            fetch('/api/quiz')
                .then(response => response.json())
                .then(data => {
                    this.questions = data.questions;
                })
                .catch(error => {
                    console.error('Error fetching questions:', error);
                });
        },
        nextQuestion() {
            // Save the selected answer
            if (this.selectedOption !== '') {
                this.questions[this.currentQuestionIndex].selectedAnswer = this.selectedOption;
            }

            // Move to the next question or show the score
            if (this.currentQuestionIndex < this.questions.length - 1) {
                this.currentQuestionIndex++;
                this.selectedOption = ''; // Reset selected option for the next question
            } else {
                this.submitQuiz();
            }
        },
        submitQuiz() {
            // Calculate the score
            this.score = this.calculateScore();
            this.showScore = true;
        },
        calculateScore() {
            let score = 0;
            for (const question of this.questions) {
                if (question.selectedAnswer === question.correctAnswer) {
                    score++;
                }
            }
            return score;
        },
        restartQuiz() {
            // Reset quiz state
            this.currentQuestionIndex = 0;
            this.selectedOption = '';
            this.showScore = false;
            this.score = 0;
            for (const question of this.questions) {
                question.selectedAnswer = '';
            }
        }
    },
    created() {
        // Fetch questions when the component is created
        this.fetchQuestions();
    }
});

app.mount('#app');