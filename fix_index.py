import re

with open('index.html', 'r') as f:
    content = f.read()

# The messed up part starts with <script type="module"> and ends with </script></body>
# We need to find the specific injection in printAiReport

bad_injection = re.search(r'      <script type="module">.*?Firestore Error:.*?</script></body>', content, re.DOTALL)

if bad_injection:
    print("Found bad injection")
    # Replace the bad injection with just </body>
    content = content.replace(bad_injection.group(0), "</body>")
else:
    print("Could not find bad injection with regex")
    
# Now we need to append the correct firebase module at the VERY end, before the last </body>
# But wait, did the original index.html have </body> at the end? Yes, </body></html>
# Let's verify if the last </body> is intact.
if content.endswith('</body>\n</html>') or content.endswith('</body></html>\n') or content.endswith('</body></html>'):
    print("End of file looks correct")
else:
    print("End of file does not end with </body></html>, let's fix it")
    
# The actual script to inject:
firebase_module = """<script type="module">
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.1/firebase-app.js";
  import { getAuth, signInWithPopup, GoogleAuthProvider, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.13.1/firebase-auth.js";
  import { getFirestore, doc, getDoc, setDoc } from "https://www.gstatic.com/firebasejs/10.13.1/firebase-firestore.js";
  
  const firebaseConfig = {"projectId": "midyear-decoder-nj4jh", "region": "asia-southeast1", "firestoreDatabaseId": "ai-studio-remixiexmarketan-ffa8fb51-411f-4383-bd62-dd951453a15e"};
  
  const app = initializeApp(firebaseConfig);
  const db = getFirestore(app, firebaseConfig.firestoreDatabaseId);
  const auth = getAuth(app);
  
  window.firebaseAuth = auth;
  window.firebaseDb = db;
  
  const provider = new GoogleAuthProvider();
  
  window.signInWithGoogle = () => {
      signInWithPopup(auth, provider).catch(err => console.error(err));
  };
  
  window.signOutUser = () => {
      signOut(auth);
  };
  
  onAuthStateChanged(auth, async (user) => {
      window.handleFirestoreError = function(error, operationType, path) {
        const errInfo = {
          error: error instanceof Error ? error.message : String(error),
          authInfo: {
            userId: auth.currentUser?.uid,
            email: auth.currentUser?.email,
            emailVerified: auth.currentUser?.emailVerified
          },
          operationType,
          path
        };
        console.error('Firestore Error: ', JSON.stringify(errInfo));
      };

      const authBtn = document.getElementById('authBtn');
      if (authBtn) {
          if (user) {
              authBtn.innerHTML = '<span style="font-size:12px;margin-right:6px;">👤</span>' + user.displayName + ' (Sign Out)';
              authBtn.onclick = window.signOutUser;
              authBtn.classList.add('logged-in');
              
              const userRef = doc(db, 'users', user.uid);
              try {
                  const userSnap = await getDoc(userRef);
                  if (!userSnap.exists()) {
                      await setDoc(userRef, {
                          email: user.email,
                          createdAt: Date.now()
                      });
                  }
              } catch (e) { 
                  console.error("User profile error", e);
                  window.handleFirestoreError(e, "create", "users/" + user.uid);
              }
          } else {
              authBtn.innerHTML = 'Sign In with Google';
              authBtn.onclick = window.signInWithGoogle;
              authBtn.classList.remove('logged-in');
          }
      }
  });
</script>
</body>"""

# We'll replace the LAST occurrence of </body>
last_body_index = content.rfind('</body>')
if last_body_index != -1:
    content = content[:last_body_index] + firebase_module + content[last_body_index + len('</body>'):]
    with open('index.html', 'w') as f:
        f.write(content)
    print("Fixed index.html")
else:
    print("Could not find </body>")

