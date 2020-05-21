static int m_int_val1;
int g_int_val1;
static const long m_const_long_val2;
const long g_const_long_val2;
static volatile char volatile_char_val3;    //static_variable_prefix NG
volatile char l_volatile_char_val3;         //global_variable_prefix NG
static int m_function_def2(char);
void g_function_def1(char flag){
    malloc();
    g_function_def1();
    if(flag){
        g_function_def1();
    }
    while(true){
        g_function_def1();
    }
    for(int i = 0; i< 10; i++){
        g_function_def1();
    }
    switch(flag){
        case 0:
            break;
        case 1:
            //No Break
        default:
            g_function_def1();
            break;
    }
    free();
    return g_function_def1();
}
static int m_function_def2(char flag2){
    while(true){
        switch(flag2){
            case 0:
                break;
            case 1:
                break;
            //No Default
        }
    }
    g_function_def1();
    return 0;
}
