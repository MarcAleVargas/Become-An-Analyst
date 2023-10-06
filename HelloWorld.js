console.log("\nhello, world\n");

function soluction(data){
    values = Math.max(...data.slice(1).map((x,i)=>[x*data[i]]));
    return values
}
console.log(soluction([3, 6, -2, -5, 7, 3]))