const importance = function(num) {
    if (num < 3) return 'indigo';
    if (num < 5) return 'teal';
    if (num < 7) return 'green';
    if (num < 9) return 'orange';
    return 'red';
}

export default importance;