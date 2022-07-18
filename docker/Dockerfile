FROM jenkins/jenkins:latest
USER root
RUN apt-get update \
        && DEBIAN_FRONTEND=noninteractive apt-get install --quiet --yes python3-dev python3-pip python3-jenkins cmake\
        && apt-get autoremove --quiet --yes \
        && apt-get clean --quiet --yes
USER jenkins
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
ENV CASC_JENKINS_CONFIG /var/jenkins_home/casc.yaml
COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt


COPY casc.yaml /var/jenkins_home/casc.yaml
COPY manage_seed.py /var/jenkins_home/manage_seed.py



