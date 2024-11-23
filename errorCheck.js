// function pengecek error
// nested condition
// clean code || refactor

const checkErrorWithCleanCode = () => {
    let error;
    if (!OK(Run1)) return error = Run1Err;
    if (!OK(Run2)) return error = Run2Err;
    if (!OK(Run3)) return error = Run3Err;
    if (!OK(Run4)) return error = Run4Err;
    return error;
}

function errorCheck() {
    let error;
    if (OK(Run1())) {
        if (OK(Run2())) {
            if (OK(Run3())) {
                if (OK(Run4())) {
                }
                else {
                    error = Run4Err;
                }
            }
            else {
                error = Run3Err;
            }
        }
        else {
            error = Run2Err;
        }
    }
    else {
        error = Run1Err;
    }
    return error;
}