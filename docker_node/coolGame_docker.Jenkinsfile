pipeline {
   //agent any
   agent {
        docker {
            label 'dockerhost'
            image 'yesubabugude/cool-node'
            //registryUrl 'https://docker-virtual.mkmartifactory.amd.com/'
            args  '-v /jenkins/bin:/jenkins/bin -v /etc/resolv.conf.amd:/etc/resolv.conf:ro -v /jenkins/.repoconfig:/.repoconfig -v /jenkins/.gitconfig:/jenkins/.gitconfig -v /jenkins/.ssh/config:/jenkins/.ssh/config:ro -v /jenkins/.ssh/known_hosts:/jenkins/.ssh/known_hosts -v /jenkins/.ssh/id_rsa:/jenkins/.ssh/id_rsa:ro'
        }
    }
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

