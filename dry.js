// make it dry

class Worker {
    constructor(hoursWorker, rate){
        this.hoursWorker = hoursWorker;
        this.rate = rate;
        this.TAX = 20;
    }

    basicSalary() {
        return this.hoursWorker * this.rate;
    }
    
    overViewSalary() {
        return this.basicSalary() + this.TAX;
    }
}

const hilman = new Worker(40, 2);
console.log(hilman.basicSalary());
console.log(hilman.overViewSalary());
