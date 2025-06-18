

PAGE_MAPPING = {
     '/_b_a_c_k_e_n_d/casualty/patient/': 'ER-P-CF',
    '/_b_a_c_k_e_n_d/casualty/register/': 'ER-P-RE',
    '/_b_a_c_k_e_n_d/casualty/next-bill-number/': 'ER-P-CF',
    '/_b_a_c_k_e_n_d/casualty/next-er-number/': 'ER-P-ER',
    '/_b_a_c_k_e_n_d/casualty/dashboard/': 'ER-P-DSH',
    '/_b_a_c_k_e_n_d/casualty/procedures/': 'ER-P-CF',
    '/_b_a_c_k_e_n_d/casualty/doctors/': 'ER-P-DOC',
    '/_b_a_c_k_e_n_d/casualty/printbill/': 'ER-P-PB',
    '/_b_a_c_k_e_n_d/casualty/patients-by-date/':'ER-P-PL',
    
    'patient/': 'ER-P-CF',
    'register/': 'ER-P-RE',
    'next-bill-number/': 'ER-P-CF',
    'next-er-number/': 'ER-P-ER',
    'dashboard/': 'ER-P-DSH',
    'procedures/': 'ER-P-CF',
    'doctors/':'ER-P-DOC',
    'printbill/': 'ER-P-PB',
    'patients-by-date/':'ER-P-PL'
}



PAGE_ACTION_MAPPING = {
    'xxx': {
        'DELETE':'RWD',
    },
}

GEN_ACTION_MAPPING = {
    'POST': 'RW',
    'PUT': 'RW',
    'DELETE': 'RW',
    'GET': 'R',
}