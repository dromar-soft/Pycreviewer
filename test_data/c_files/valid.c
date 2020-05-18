static int m_int_val1;
int g_int_val1;
static const long m_const_long_val2;
const long g_const_long_val2;
static volatile char m_volatile_char_val3;
volatile char g_volatile_char_val3;
static int m_function_def2(char);
void g_function_def1(char flag){
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
            break;
        default:
            g_function_def1();
            break;
    }
    return g_function_def1();
}
static int m_function_def2(char c){
    return 0;
}
