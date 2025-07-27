import subprocess
import psutil
import os

class SystemMonitor:
    def __init__(self):
        self.initial_state = {}
    
    def capture_initial_state(self):
        self.initial_state['processes'] = [p.info for p in psutil.process_iter(['pid', 'name'])]
        self.initial_state['files'] = self._get_file_hashes()
    
    def _get_file_hashes(self):
        files = {}
        for root, _, filenames in os.walk(os.getcwd()):
            for filename in filenames:
                filepath = os.path.join(root, filename)
                files[filepath] = self._get_file_hash(filepath)
        return files
    
    def _get_file_hash(self, filepath):
        try:
            with open(filepath, 'rb') as f:
                return hash(f.read())
        except:
            return None
    
    def get_changes(self):
        current_state = {
            'processes': [p.info for p in psutil.process_iter(['pid', 'name'])],
            'files': self._get_file_hashes()
        }
        return {
            'new_processes': [p for p in current_state['processes'] if p not in self.initial_state['processes']],
            'modified_files': {k: v for k, v in current_state['files'].items() 
                             if k in self.initial_state['files'] and v != self.initial_state['files'][k]}
        }