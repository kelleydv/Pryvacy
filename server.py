#!/usr/bin/env python3
from pryvacy import app
import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
