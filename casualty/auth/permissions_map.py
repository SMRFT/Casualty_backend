


PAGE_MAPPING = {
     '_b_a_c_k_e_n_d/casualty/patient/': 'ER-P-PL-RW',
    '_b_a_c_k_e_n_d/casualty/patients/register/': 'ER-P-PR-RW',
    '_b_a_c_k_e_n_d/casualty/next-bill-number/': 'ER-P-BILL-R',
    '_b_a_c_k_e_n_d/casualty/next-er-number/': 'ER-P-ER-R',
    '_b_a_c_k_e_n_d/casualty/dashboard/': 'ER-P-DSH-R',
    '_b_a_c_k_e_n_d/casualty/procedures/': 'ER-P-PRC-R',
    '_b_a_c_k_e_n_d/casualty/doctors/': 'ER-P-DOC-R',
    '_b_a_c_k_e_n_d/casualty/patient-by-er/': 'ER-P-ERF-R',
    '_b_a_c_k_e_n_d/casualty/patients-by-date/': 'ER-P-PDATE-R',
    '_b_a_c_k_e_n_d/casualty/printbill/': 'ER-P-PB-R',


    'patient/': 'ER-P-PL-RW',
    'patients/register/': 'ER-P-PR-RW',
    'next-bill-number/': 'ER-P-BILL-R',
    'next-er-number/': 'ER-P-ER-R',
    'dashboard/': 'ER-P-DSH-R',
    'procedures/': 'ER-P-PRC-R',
    'doctors/': 'ER-P-DOC-R',
    'patient-by-er/': 'ER-P-ERF-R',
    'patients-by-date/': 'ER-P-PDATE-R',
    'printbill/': 'ER-P-PB-R'
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