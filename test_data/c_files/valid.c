static int m_int_val1;
int g_int_val1;
static const long m_;                       //variable_length_min NG
const long g_;                              //variable_length_min NG
static volatile char volatile_char_val3;    //static_variable_prefix NG
volatile char l_volatile_char_val3;         //global_variable_prefix NG
static int m_function_def2(char);
void g_function_def1(char flag){
    malloc(); //function_blacklist NG
    g_function_def1();
    if(flag){
        g_function_def1();
    }
    while(true){
        g_function_def1();
    }
    for(int i = 0; i< 10; i++){            //variable_length_min NG
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
    free(); //function_blacklist NG
    return g_function_def1();
}
static int m_function_def2(char f){         //variable_length_min NG
    while(true){
        switch(f){
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
