

const getLastWeeksDate = () => {
    const weekDays = [];
    const curr = new Date();
    const first = curr.getDate() - curr.getDay() - 4;


    for (let i = first; i < first + 7; i++) {
        const day = new Date(curr.setDate(i)).toISOString().slice(0, 10);
        weekDays.push(day);
    }
    return weekDays;

}




export default getLastWeeksDate;