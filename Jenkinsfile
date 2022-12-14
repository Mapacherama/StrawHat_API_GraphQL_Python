properties([parameters(
[string(defaultValue: 'NameofScan', description: 'Use only alphabets, without space', name: 'SCAN_NAME', trim: true), string(defaultValue: 'git@abc.com:test/repo1.git', description: 'Enter the "Clone with SSH" url', name: 'REPO', trim: true),
string(defaultValue: 'dev', description: 'Select the release branch to run scans for particular release', name: 'Branch', trim: true),
choice(choices: ['YES', 'NO'], description: 'Run normal scan', name: 'NORMAL_SCAN'),
choice(choices: ['YES', 'NO'], description: 'Run baseline scan to hide previous found issues. If you choose YES you MUST upload baseline json file in next step.', name: 'BASELINE_SCAN'),
file(description: 'Upload the bandit baseline json file to ignore old issues', name: 'BASELINE_JSON'),
choice(choices: ['YES', 'NO'], description: 'Choose YES to generate baseline json file, which can be uploaded next time you run the scan to hide issues found in this scan.', name: 'CREATE_BASELINE')
])])
pipeline {
    agent {
        docker { image 'python:3.10.0-alpine'
                 args '-u root:sudo'
            }
    }
    stages {
        stage('Install Bandit') {
            steps {
                sh "pip install bandit"
            }
        }
        stage ('Run Bandit Scan') {
            when {
                expression {params.NORMAL_SCAN == "YES"}
            }
            steps {
                timestamps{ echo ">>>>>>>>>>Running bandit on repo ${params.repo}>>>>>>>>>>>>>>>>>>>>" }
                git branch: "${params.Branch}",
                credentialsId: "****",
                url: "${params.REPO}"
                sh label: '', returnStatus: true, script: """
                        bandit -r -f html -o bandit_report_${params.SCAN_NAME}.html .
                        """
                }
        }

        stage ('Run Bandit Baseline Scan') {
            when {
                expression {params.BASELINE_SCAN == "YES"}
            }
            steps {
                timestamps{ echo ">>>>>>>>>>Running bandit baseline scan on repo ${params.REPO}>>>>>>>>>>>>>>>>>>>>" }
                git branch: "${params.Branch}",
                credentialsId: "****",
                url: "${params.REPO}"
                script{
                    @Library('jenkinsci-unstashParam-library@master') _
                    def file_in_workspace = unstashParam "BASELINE_JSON"
                    sh label: '', returnStatus: true, script: """
                    bandit -r -f html -o bandit_report_${params.SCAN_NAME}.html -b ${file_in_workspace} .
                    """
                    sh "rm -rf ${file_in_workspace}"
                }
            }
        }
        stage ('Create Bandit baseline') {
            when {
                expression {params.CREATE_BASELINE == "YES"}
            }
            steps {
                sh label: '', returnStatus: true, script: """
                    bandit -r -f json -o bandit_baseline_${params.SCAN_NAME}.json .
                    """
            }
        }
        stage ('Archive report') {
            steps {
                archiveArtifacts artifacts: 'bandit_*.*'
                deleteDir()
            }
        }
    }
}