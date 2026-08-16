import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 20,
  duration: '2m',
  thresholds: {
    http_req_duration: ['p(95)<1000'],
    http_req_failed: ['rate<0.01'],
  },
};

const BASE_URL = __ENV.TARGET_URL || 'http://<gcp-lb-ip>';

const predictPayload = {
  tenure: 12,
  monthly_charges: 65.5,
  total_charges: 786.0,
  contract: 'Month-to-month',
  payment_method: 'Electronic check',
};

export default function () {
  // 70% GET /health, 30% POST /predict
  if (Math.random() < 0.7) {
    const res = http.get(`${BASE_URL}/health`);
    check(res, { 'health status 200': (r) => r.status === 200 });
  } else {
    const res = http.post(
      `${BASE_URL}/predict`,
      JSON.stringify(predictPayload),
      { headers: { 'Content-Type': 'application/json' } }
    );
    check(res, {
      'predict status 200': (r) => r.status === 200,
      'predict has prediction': (r) => JSON.parse(r.body).prediction !== undefined,
    });
  }
  sleep(1);
}