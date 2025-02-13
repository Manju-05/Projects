const Quiz_Container = document.getElementById("Quiz-Container")
const QuestionElement = document.getElementById("Questions")
const OptionsElement = document.getElementById("Options")
const submitBtnElement = document.getElementById("SubmitBtn")
const feedbackElement = document.getElementById("feedback")
const scoreElement = document.getElementById("Score")
const heading = document.getElementById("heading")


let currentquestionindex = 0;
let score = 0 ;

// creating the [array] of 
// {objects ==> question , options, correctanswer }

let Quiz_qestions = [
    {
        Question: " Which of the following is referred to as the brain of a computer?",
        options: ["a. RAM", "b. ROM", "c. MONITER", "d. CPU"],
        correctAnswer: "d. CPU"
    },
    {
        Question: "- If you restart your computer by switching it off (i.e. power cut), it is known as …",
        options: ["a. SoftBoot ", "b. ColdBoot", "c. WarmBoot", "d. a & b"],
        correctAnswer: "b. ColdBoot"
    },
    {
        Question: "Which of the following computer language used for artificial intelligence?",
        options: ["a. PROLOG", "b. FORTRAN", "c. C", "d. COBOL"],
        correctAnswer: "a. PROLOG"    
    },
    {
        Question: " Which among the following is the shortcut key to open a new window?",
        options: ["a. Shift + N", "b. ctrl + N", "c. alt + N", "d. alt f5"],
        correctAnswer: "b. ctrl + N"
    },
    {
        Question: " Which among the following types of memories get refreshed several times per second?" ,
        options: ["a. ROM", "b. D-RAM", "c. S-RAM", "d. CacheMemory"],
        correctAnswer: "b. ctrl + N"
    },
    {
        Question: "  A pictorial representation of a program or the algorithm is known as" ,
        options: ["a. User", "b. Host", "c.Internet user", "d.  Guest"],
        correctAnswer: "b. Host"
    },
    {
        Question: "   In an internet world, each computer is known as …" ,
        options: ["a. Diagram", "b. Flowchart", "c. Data flow", "d.  Data"],
        correctAnswer: "b. Flowchart"
    },
    {
        Question: " Who is the Father of Computer?" ,
        options: ["a. Fernado", "b. guidoRussom", "c. Einsten", "d. Babbage"],
        correctAnswer: "d.Babbage"
    }
];

function loadQuestions() {
    // creating the question and appending it to the page..
    const currentquestion = Quiz_qestions[currentquestionindex];
    QuestionElement.innerHTML = currentquestion.Question

    OptionsElement.textContent = "";

    // creating the options and appending it to the page
    // retrvivng the options from the currentquestion and iterating it

    currentquestion.options.forEach((option, index) => {
        const optionbuttons = document.createElement("button");
        optionbuttons.innerHTML = option;

        optionbuttons.onclick = function () {
            selectAnswer(option, currentquestion.correctAnswer);
        }

        OptionsElement.appendChild(optionbuttons)
    })
}


function selectAnswer(selectedOption, correctAnswer) {
    if (selectedOption === correctAnswer) {
        feedbackElement.innerHTML = "CorrectAnswer✅";
        score++;
        scoreElement.innerHTML = `Score : ${score}`
    }
    else {
        feedbackElement.innerHTML = "OOPS!! Wrong Answer " + "correct Answer :" + correctAnswer;
    }
    currentquestionindex++;
    
    if (currentquestionindex < Quiz_qestions.length) {
        loadQuestions();
    }
    else {
        endquiz()  
    }
}

function endquiz(){
    console.log("quiz ended")
    Quiz_Container.innerHTML = "<h2>Quiz Completed..!🚀🔄️</h2>";
    scoreElement.innerHTML = "FinalScore :" + score + " out of " + Quiz_qestions.length;
}

// function submitAnswer() {
//     const selectedOption = document.querySelector('input[name="option"]:checked');
//     if (selectedOption) {
//         selectAnswer(selectedOption.value);
//     }
// }

loadQuestions()
