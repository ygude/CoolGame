pipeline {
   agent any
   stages {
        stage('Checkout') {
            steps {
             // Clean before build
                cleanWs()
            	dir("CoolGame"){
            	sh "echo credentials: ${CREDENTIALS_ID}"
                checkout([$class: 'GitSCM', branches: [[name: '${BRANCH}']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: "${CREDENTIALS_ID}", url: '${PROJECT_REPO}.git']]])
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
	    		dir("CoolGame"){
	    		sh '''
				cd build/game/src/test
				./CoolGame_tst
				
				if [ $? -eq 0 ]
				then
				   echo "All Tests are Passed"
				else
				   echo "Looks like test(s) failed"
				fi
	    		'''
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
