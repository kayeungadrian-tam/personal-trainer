import axios from 'axios';

const get_quiz = async () => {
    const url = "https://the-trivia-api.com/api/questions?limit=2"

    const respone = await axios.get(url);
    console.log(respone)
    return respone
};



export default get_quiz;