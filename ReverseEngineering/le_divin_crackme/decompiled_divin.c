void _init()
{
    if (__gmon_start__ != 0)
    {
        __gmon_start__();
    }
}

int64_t sub_1020()
{
    int64_t var_8 = data_3ff0;
    /* jump -> data_3ff8 */
}

int32_t strncmp(char const* arg1, char const* arg2, uint64_t arg3)
{
    /* tailcall */
    return strncmp(arg1, arg2, arg3);
}

int64_t sub_1036()
{
    int64_t var_8 = 0;
    /* tailcall */
    return sub_1020();
}

uint64_t strlen(char const* arg1)
{
    /* tailcall */
    return strlen(arg1);
}

int64_t sub_1046()
{
    int64_t var_8 = 1;
    /* tailcall */
    return sub_1020();
}

int32_t printf(char const* format, ...)
{
    /* tailcall */
    return printf();
}

int64_t sub_1056()
{
    int64_t var_8 = 2;
    /* tailcall */
    return sub_1020();
}

int32_t __isoc99_scanf(char const* format, ...)
{
    /* tailcall */
    return __isoc99_scanf();
}

int64_t sub_1066()
{
    int64_t var_8 = 3;
    /* tailcall */
    return sub_1020();
}

void __cxa_finalize(void* d)
{
    /* tailcall */
    return __cxa_finalize(d);
}

int64_t _start(int64_t arg1, int64_t arg2, void (* arg3)()) __noreturn
{
    int64_t rax;
    int64_t var_8 = rax;
    __libc_start_main(main, __return_addr, &arg_8, nullptr, nullptr, arg3, &var_8);
    /* no return */
}

void deregister_tm_clones()
{
    return;
}

void register_tm_clones()
{
    return;
}

void __do_global_dtors_aux()
{
    if (__TMC_END__ != 0)
    {
        return;
    }
    if (__cxa_finalize != 0)
    {
        __cxa_finalize(__dso_handle);
    }
    deregister_tm_clones();
    __TMC_END__ = 1;
}

void frame_dummy()
{
    /* tailcall */
    return register_tm_clones();
}

int32_t main(int32_t argc, char** argv, char** envp)
{
    int32_t var_4c = argc;
    char** var_58 = argv;
    printf("Mot de passe ? : ");
    void var_48;
    __isoc99_scanf("%60s", &var_48);
    int32_t rax_7;
    if (strlen(&var_48) != 0x1e)
    {
    label_124c:
        printf(&data_2078);
        rax_7 = 1;
    }
    else
    {
        void var_3e;
        if (strncmp(&var_3e, "Ph13_d4N5_", 0xa) != 0)
        {
            goto label_124c;
        }
        if (strncmp(&var_48, "L4_pH1l0so", 0xa) != 0)
        {
            goto label_124c;
        }
        void var_34;
        if (strncmp(&var_34, "l3_Cr4cKm3", 0xa) != 0)
        {
            goto label_124c;
        }
        printf(&data_2040);
        rax_7 = 0;
    }
    return rax_7;
}

int64_t _fini()
{
    return;
}


