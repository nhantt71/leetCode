/**
 * @param {number[]} distance
 * @param {number} start
 * @param {number} destination
 * @return {number}
 */
var distanceBetweenBusStops = function(distance, start, destination) {
    var flow = 0;
    var reverse = 0;
    if(start > destination){
        var temp = start;
        start = destination;
        destination = temp;
    }
    const arr1 = distance.slice(start, destination);
    arr1.forEach((x) => flow += x);
    distance.forEach((x) => reverse += x);
    reverse = reverse - flow;

    return flow > reverse ? reverse : flow;
};