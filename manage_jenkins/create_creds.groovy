import com.cloudbees.plugins.credentials.impl.*
import com.cloudbees.plugins.credentials.*
import com.cloudbees.plugins.credentials.domains.*
import com.cloudbees.jenkins.plugins.sshcredentials.impl.*

def source = new BasicSSHUserPrivateKey.DirectEntryPrivateKeySource("key")
def ck1 = new BasicSSHUserPrivateKey(CredentialsScope.GLOBAL, "SSH_CREDS", "ygude", source, "", "Replace your key + username")

SystemCredentialsProvider.getInstance().getStore().addCredentials(Domain.global(), ck1)
