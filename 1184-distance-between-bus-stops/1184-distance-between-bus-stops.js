/**
 * @param {number[]} distance
 * @param {number} start
 * @param {number} destination
 * @return {number}
 */
var distanceBetweenBusStops = function(distance, start, destination) {
    var flow = 0;
    if(start > destination){
        var temp = start;
        start = destination;
        destination = temp;
    }
    distance.slice(start, destination).forEach((x) => flow += x);
    var reverse = distance.reduce((acc, cur) => {return acc + cur;});
    reverse = reverse - flow;

    return flow > reverse ? reverse : flow;
};