pipeline {
   agent any
   stages {
        stage('Checkout') {
            steps {
                cleanWs()
            	dir("CoolGame"){
					sh "echo credentials: ${CREDENTIALS_ID}"
					checkout(
						[$class: 'GitSCM', 
						branches: [[name: '${BRANCH}']], 
						doGenerateSubmoduleConfigurations: false, 
						extensions: [], 
						submoduleCfg: [], 
						userRemoteConfigs: [[credentialsId: "${CREDENTIALS_ID}", url: '${PROJECT_REPO}.git']]]
					)
            	}
           }
        }
    	stage("Build"){
    		steps {
	    		dir("CoolGame"){
					sh '''
						mkdir -p build
						cmake -Bbuild -DCMAKE_BUILD_TYPE=Release
						cd build
						make
						if [ $? -eq 0 ]
						then
						echo "Compiled Successful!"
						else
						echo "Compilation failed!"
						fi
					'''
	    		}
	    	}
    	}
    	
    	stage("Tests"){
    		steps {
    			script {
		    		dir("CoolGame"){
						try {
						sh '''
							cd build/game/src/test
							./CoolGame_tst
							echo "Tests are Passed!"
						'''   		
						}
						catch(err)
						{
							sh 'echo "Test(s) failed"'
							currentBuild.result = 'UNSTABLE'
						}
	    			}
				}
	    	}
    	}
    	
    	stage("Archive"){
    		steps {
	    		dir("CoolGame/build/game/src/test"){
	    			archiveArtifacts artifacts: 'CoolGame_tst'
	    		}
	    		dir("CoolGame/build/game"){
	    			archiveArtifacts artifacts: 'CoolGame_run'
	    		}
	    	}
    	}    	
    }
}